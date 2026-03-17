
provision:
	minkube start
	find manifests -name '*.yaml' -print0 | xargs -0 -n1 kubectl apply -f