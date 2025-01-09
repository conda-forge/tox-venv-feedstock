import sys
from subprocess import call

FAIL_UNDER = "68"
COV = ["coverage"]
RUN = ["run", "--source=tox_venv", "--branch", "-m"]
PYTEST = ["pytest", "-vv", "--color=yes", "--tb=long"]
REPORT = ["report", "--show-missing", "--skip-covered", f"--fail-under={FAIL_UNDER}"]

SKIPS = [
    "test_create",
    "test_develop_extras",
    "test_matchingdependencies_latest",
    "test_missing_env_fails",
    "test_no_setup_py_exits",
    "test_notoxini_help_still_works",
    "test_result_json",
    "test_run_custom_install_command",
]

#: added in https://github.com/conda-forge/tox-feedstock/pull/185
SKIPS += ["load_dependency_many_extra"]

SKIP_OR = " or ".join(SKIPS)
K = ["-k", f"not ({SKIP_OR})"]


if __name__ == "__main__":
    sys.exit(
        # run the tests
        call([*COV, *RUN, *PYTEST, *K])
        # maybe run coverage
        or call([*COV, *REPORT])
    )
