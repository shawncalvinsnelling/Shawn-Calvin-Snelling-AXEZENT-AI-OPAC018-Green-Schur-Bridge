# External Review Packet Checklist

Before sending to an outside reviewer, confirm:

- [ ] `python verify_manifest.py` passes.
- [ ] `python pure_python_exact_audit.py` passes.
- [ ] `python counterexample_stress_test.py` passes.
- [ ] GitHub Actions are green.
- [ ] The latest GitHub release matches the files being reviewed.
- [ ] The README states `solution-candidate` and `external review pending`.
- [ ] No wording claims P vs NP, RH, TSP, journal acceptance, or historical recognition.
- [ ] The reviewer is pointed to `REFEREE_ROADMAP.md` first.
- [ ] The reviewer knows the code is audit support, not proof replacement.
