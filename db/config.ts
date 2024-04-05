import { defineDb, defineTable, column, NOW } from 'astro:db';

const CS2Leaderboard = defineTable({
  columns: {
    // User
    id: column.text({ primaryKey: true }), // faceit id
    nickname: column.text(),
    profileLink: column.text(), // might not need this
    // Stats
    position: column.number(),
    faceit_elo: column.number(),
    game_skill_level: column.number(),
    movement: column.number(), // 0 = no change, 1 = up, -1 = down
    // Metadata
    createdAt: column.date({ default: NOW }),
    updatedAt: column.date({ optional: true }),
    deletedAt: column.date({ optional: true }),

  },
  indexes: {
    user_idx: { on: ["id"], unique: true }
  },

  
})

export default defineDb({
  tables: {
    CS2Leaderboard
  }
});
