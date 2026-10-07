import { defineConfig } from 'astro/config';

export default defineConfig({
  site: process.env.SITE_URL || 'https://jdistlr.github.io',
  base: process.env.BASE_PATH || '/kleines-schaeferrad',
  trailingSlash: 'always',
  output: 'static',
});
