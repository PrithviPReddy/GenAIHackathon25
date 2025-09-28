from typing import List
import re
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.utils.logger import logger


class ImprovedTextChunker:
    """Enhanced text chunking with better strategies for legal documents"""
    
    def __init__(self, chunk_size: int = 800, overlap: int = 150):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap,
            length_function=len,
            separators=[
                "\n=== Page",    # Page breaks
                "\n\n",         # Paragraph breaks
                "\nArticle",    # Article breaks for constitution
                "\nSection",    # Section breaks
                "\nChapter",    # Chapter breaks
                ".\n",          # Sentence breaks
                "\n",           # Line breaks
                " ",            # Word breaks
                ""              # Character breaks
            ]
        )
    
    def chunk_text(self, text: str) -> List[str]:
        """Split text into overlapping chunks with improved preprocessing"""
        try:
            cleaned_text = self.preprocess_text(text)
            
            chunks = self.text_splitter.split_text(cleaned_text)
            
            processed_chunks = []
            for chunk in chunks:
                processed_chunk = self.postprocess_chunk(chunk)
                if len(processed_chunk.strip()) > 100:  
                    processed_chunks.append(processed_chunk)
            
            logger.info(f" Created {len(processed_chunks)} processed chunks from text")
            return processed_chunks
            
        except Exception as e:
            logger.error(f" Failed to chunk text: {e}")
            return []
    
    def preprocess_text(self, text: str) -> str:
        """Clean and preprocess text for better chunking"""
        text = text.replace('\x00', '')
        
        text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
        
        text = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', text)
        
        text = re.sub(r'\b(Article|Section|Chapter)\s+(\d+)', r'\n\1 \2', text)
        
        return text.strip()
    
    def postprocess_chunk(self, chunk: str) -> str:
        """Clean up individual chunks"""
        chunk = re.sub(r'^=== Page \d+ ===\s*', '', chunk)
        chunk = re.sub(r'\s*=== Page \d+ ===$', '', chunk)
        chunk = re.sub(r'\s+', ' ', chunk)
        chunk = chunk.strip()
        
        return chunk


