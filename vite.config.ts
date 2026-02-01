import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { viteSingleFile } from "vite-plugin-singlefile"

// https://vitejs.dev/config/
export default defineConfig({
  base: './',
  plugins: [react(), viteSingleFile(), {
    name: 'remove-crossorigin',
    transformIndexHtml(html) {
      return html.replace(' type="module" crossorigin', ' type="module"');
    }
  }],
  build: {
      target: 'es2015',
      assetsInlineLimit: 100000000, // Inline all assets up to 100MB
    },
})
