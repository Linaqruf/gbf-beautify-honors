# Reference: https://stackoverflow.com/a/14061796
# If the first argument is "version"
ifeq (version,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "version"
  VERSION_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(VERSION_ARGS):;@:)
endif

.PHONY: version
version:
	@poetry version $(VERSION_ARGS)
	@git add pyproject.toml
	@git commit -m "chore: Bumping version to $$(poetry version -s)"
	@git tag "$$(poetry version -s)"
	@echo
	@echo "Please run 'git push --follow-tags' to update remote."
