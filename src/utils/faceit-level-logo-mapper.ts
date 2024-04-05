// Create a record mapping for Logos based on level (number)

import type { ImageMetadata } from 'astro';

import {
    FACEIT_LEVEL1,
    FACEIT_LEVEL2,
    FACEIT_LEVEL3,
    FACEIT_LEVEL4,
    FACEIT_LEVEL5,
    FACEIT_LEVEL6,
    FACEIT_LEVEL7,
    FACEIT_LEVEL8,
    FACEIT_LEVEL9,
    FACEIT_LEVEL10
} from '../assets/faceit-levels/index.ts';

export const FACEIT_LEVEL_LOGOS: Record<number, ImageMetadata> = {
    1: FACEIT_LEVEL1,
    2: FACEIT_LEVEL2,
    3: FACEIT_LEVEL3,
    4: FACEIT_LEVEL4,
    5: FACEIT_LEVEL5,
    6: FACEIT_LEVEL6,
    7: FACEIT_LEVEL7,
    8: FACEIT_LEVEL8,
    9: FACEIT_LEVEL9,
    10: FACEIT_LEVEL10
}