function generateHtml() {
  let ref1, ref2, ref3;
  return {
    buildStart() {
      ref1 = this.emitFile({
        type: "chunk",
        id: "main.js",
      });
    },
    generateBundle() {
      this.emitFile({
        type: "asset",
        fileName: "index.html",
        source: `
      <!DOCTYPE html>
      <html>
      <head>
        <meta charset="UTF-8">
        <title>Title</title>
       </head>
      <body>
        <script src="${this.getFileName(ref1)}" type="module"></script>
      </body>
      </html>
      `,
      });
    },
  };
}

module.exports = {
  build: {
    outDir: "../static/frontend/",
    rollupOptions: {
      plugins: [generateHtml()],
    }
  },
};
