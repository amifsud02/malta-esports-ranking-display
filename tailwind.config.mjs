import { fontFamily } from "tailwindcss/defaultTheme";

/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			fontFamily: {
				sans: ["var(--font-neue-kaine)", ...fontFamily.sans],
			}
		},
		colors: {
			'white': '#FEFFF8',
			'lime': '#D0FE26',
			'black': '#040404',
			'purple': '#BB01FF',
		}
	},
	plugins: [],
}
