import { authMiddleware } from '@clerk/nextjs/server';

export default authMiddleware({
  // Add all public routes (routes that don't require authentication) here
  publicRoutes: [
    '/',
    '/login(.*)',
    '/signup(.*)',
    '/login/sso-callback(.*)',
    '/signup/sso-callback(.*)'
  ],
});

export const config = {
  matcher: [
    // Skip Next.js internals and all static files
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    // Always run for API routes
    '/(api|trpc)(.*)',
  ],
  // This line forces the middleware to run on the Node.js runtime
  runtime: 'nodejs',
};
