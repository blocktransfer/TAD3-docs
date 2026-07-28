# TAD3 Developer Documentation

The documentation site is built with Docusaurus.

## Local development

```shell
npm install
npm start
```

Create a production build with:

```shell
npm run build
```

## Versioned releases

The default branch is published at `https://tad3.dev/`. To preserve an
immutable historical release without copying the documentation source, tag the
release commit with a `docs-v` tag:

```shell
git tag docs-v1.0.0 <commit-sha>
git push origin docs-v1.0.0
```

The deployment workflow builds that exact commit and publishes it at
`https://tad3.dev/1.0.0/`. Existing version directories are preserved when
new versions and updates to the default site are deployed.

See BlockTransfer's public FOSS repositories:

- [Python Horizon interface](https://github.com/blocktransfer/py-tad3-horizon)
