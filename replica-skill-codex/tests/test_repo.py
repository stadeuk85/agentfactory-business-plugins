import json
import os
import re
import unittest

from _load import ROOT

SPECIALISTS = ["replica-recon", "replica-architect", "replica-design", "replica-build",
               "replica-backend", "replica-test", "replica-diff", "replica-entrepreneur",
               "replica-brand", "replica-launch", "replica-deploy"]
SKILLS = ["replica"] + SPECIALISTS


def frontmatter(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return (m.group(1) if m else ""), text


class Repo(unittest.TestCase):
    def test_twelve_skill_folders(self):
        root = os.path.join(ROOT, "skills")
        found = sorted(d for d in os.listdir(root)
                       if os.path.isfile(os.path.join(root, d, "SKILL.md")))
        self.assertEqual(found, sorted(SKILLS))

    def test_frontmatter_name_and_description(self):
        for s in SKILLS:
            fm, text = frontmatter(os.path.join(ROOT, "skills", s, "SKILL.md"))
            self.assertIn("name: %s\n" % s, fm + "\n", s)
            self.assertRegex(fm, r"description: ", s)
            self.assertGreater(len(fm), 120, "%s description is too thin" % s)
            self.assertGreater(len(text.splitlines()), 25, s)

    def test_portable_manifest(self):
        with open(os.path.join(ROOT, "plugin.json")) as fh:
            plugin = json.load(fh)
        self.assertEqual(plugin["name"], "replica-skill-codex")
        self.assertEqual(plugin["version"], "1.1.0")
        self.assertEqual(plugin["$schema"], "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json")

    def test_codex_compat_manifest(self):
        with open(os.path.join(ROOT, ".codex-plugin", "plugin.json")) as fh:
            plugin = json.load(fh)
        self.assertEqual(plugin["name"], "replica-skill-codex")
        self.assertEqual(plugin["skills"], "./skills/")
        self.assertEqual(plugin["interface"]["displayName"], "Replica Codex")

    def test_readme_has_install_and_origin(self):
        with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as fh:
            readme = fh.read()
        self.assertIn("codex plugin marketplace add stadeuk85/agentfactory-business-plugins", readme)
        self.assertIn("Jakeschincariol/replica-skill", readme)
        for s in SKILLS:
            self.assertIn("$" + s, readme)

    def test_no_em_dashes_anywhere(self):
        bad = []
        for dirpath, dirnames, filenames in os.walk(ROOT):
            dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__")]
            for fn in filenames:
                if fn.endswith((".md", ".py", ".json", ".ts", ".csv")):
                    path = os.path.join(dirpath, fn)
                    with open(path, encoding="utf-8") as fh:
                        if chr(0x2014) in fh.read():
                            bad.append(os.path.relpath(path, ROOT))
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main()
