const config = {
  title: "TAD3 Developer Documentation",
  tagline: "The Blockchain Direct Registration System",
  favicon: "img/favicon.ico",

  future: {
    v4: true,
  },

  url: "https://tad3.dev",
  baseUrl: process.env.DOCS_BASE_URL || "/",
  trailingSlash: true,

  organizationName: "blocktransfer",
  projectName: "TAD3-docs",

  onBrokenLinks: "throw",

  presets: [
    [
      "classic",
      {
        docs: {
          path: "docs/source",
          routeBasePath: "/",
          sidebarPath: "./sidebars.js",
        },
        blog: false,
        pages: false,
        theme: {
          customCss: "./src/css/custom.css",
        },
      },
    ],
  ],

  themeConfig: {
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: "TAD3",
      items: [
        {
          href: "https://github.com/blocktransfer/TAD3-docs",
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Documentation",
          items: [
            {label: "Introduction", to: "/intro"},
            {label: "Transfers", to: "/transfers"},
            {label: "API", to: "/api/overview"},
          ],
        },
        {
          title: "Community",
          items: [
            {
              label: "Developer support",
              href: "mailto:support@blocktransfer.dev",
            },
            {
              label: "GitHub",
              href: "https://github.com/blocktransfer",
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} BlockTrans Syndicate.`,
    },
  },
};

export default config;
