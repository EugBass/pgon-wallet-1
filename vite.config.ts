import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';
import { resolve } from 'path';

export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    host: '0.0.0.0',
    port: 3000,
  },
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        blog: resolve(__dirname, 'blog.html'),
        terms: resolve(__dirname, 'terms.html'),
        privacy: resolve(__dirname, 'privacy.html'),
        amlCft: resolve(__dirname, 'aml-cft.html'),
        cookies: resolve(__dirname, 'cookies.html'),
        blogChatgpt: resolve(__dirname, 'blog/kak-oplatit-chatgpt-plus-iz-rossii-2026.html'),
        blogSbp: resolve(__dirname, 'blog/kak-oplachivat-po-qr-sbp-kriptovalyutoy.html'),
        blog115Fz: resolve(__dirname, 'blog/kak-izbezhat-blokirovok-115-fz-pri-rabote-s-kriptoy.html'),
        blogSteamAppstore: resolve(__dirname, 'blog/virtualnaya-karta-dlya-app-store-i-steam.html'),
      }
    }
  }
});

