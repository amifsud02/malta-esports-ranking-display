import { defineConfig } from 'astro/config';
import vercel from "@astrojs/vercel/serverless";
import react from "@astrojs/react";
import tailwind from "@astrojs/tailwind";

import db from "@astrojs/db";

// https://astro.build/config
export default defineConfig({
  output: "server",
  adapter: vercel({
    imageService: true,
  }),
  integrations: [react(), tailwind(), db()]
});