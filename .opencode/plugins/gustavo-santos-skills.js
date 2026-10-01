import path from "node:path"
import { fileURLToPath } from "node:url"

const skillsDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../../skills")

// OpenCode scans each registered path for nested SKILL.md files, so the
// area folders (skills/goose, skills/mobile, ...) need no per-area entries.
export const GustavoSantosSkills = async () => ({
  config: async (config) => {
    config.skills = config.skills ?? {}
    config.skills.paths = config.skills.paths ?? []
    if (!config.skills.paths.includes(skillsDir)) {
      config.skills.paths.push(skillsDir)
    }
  },
})
