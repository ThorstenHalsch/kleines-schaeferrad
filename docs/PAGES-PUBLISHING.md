# GitHub Pages publishing

The research page already passes through a static Astro build pipeline on the working branch.

Deployment is intentionally **not enabled yet** because GitHub Pages has not been activated for `jdistlr/kleines-schaeferrad`. The previous deployment probe returned GitHub's expected 404 with the explicit instruction to enable Pages in repository settings.

When the user wants a public preview:

1. Open repository **Settings → Pages**.
2. Set **Source** to **GitHub Actions**.
3. Re-enable the deploy job in `.github/workflows/pages.yml` or create a dedicated preview workflow.
4. Keep the project base path `/kleines-schaeferrad`.
5. Keep `noindex, nofollow` until the research preview is intentionally public-facing.

Until then, CI proves `astro check` and `astro build` and uploads the static `dist` artifact without publication.
