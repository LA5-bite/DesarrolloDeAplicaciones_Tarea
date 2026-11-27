import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    outDir: '../backend/core/static/vite',
    emptyOutDir: true,
    rollupOptions: {
      output: {
        entryFileNames: 'app.js',
        assetFileNames: 'app.[ext]'
      }
    }
  }
});
