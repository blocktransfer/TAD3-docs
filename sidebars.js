const sidebars = {
  docs: [
    "index",
    {
      type: "category",
      label: "Introduction",
      items: ["intro"],
    },
    {
      type: "category",
      label: "TAD3 Platform",
      items: ["transfers", "governance", "markets", "oversight"],
    },
    {
      type: "category",
      label: "Capital Markets",
      items: [
        {
          type: "category",
          label: "Core concepts",
          items: [
            "regs/learn/index",
            "regs/learn/lifecycle",
            "regs/learn/investing",
            "regs/learn/insiders",
          ],
        },
        {
          type: "category",
          label: "United States",
          items: [
            "regs/us/index",
            "regs/us/144",
            "regs/us/sec-4a",
            "regs/us/144a",
            {
              type: "category",
              label: "Offerings",
              items: [
                "regs/us/offerings/index",
                "regs/us/offerings/d/506b",
                "regs/us/offerings/d/506c",
              ],
            },
          ],
        },
      ],
    },
    {
      type: "category",
      label: "Syndicate API",
      items: [
        "api/overview",
        "api/external-endpoints",
        "api/issuerlink",
        "api/operations",
      ],
    },
  ],
};

export default sidebars;
