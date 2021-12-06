//publicPath is set as vue-crypto-dashboard for production you can change it according to your application
 module.exports = {
  publicPath: process.env.NODE_ENV === 'production' ? '/vue-crypto-dashboard/' : '/' ,
  filenameHashing: false,
  devServer: {
    proxy: 'http://127.0.0.1:8000/',
}
}; 

/**
module.exports = {
  publicPath: '/static/src/vue/dist/', // Should be STATIC_URL + path/to/build
  outputDir: path.resolve(__dirname, '../static/src/vue/dist/'), // Output to a directory in STATICFILES_DIRS
  filenameHashing: false, // Django will hash file names, not webpack
  runtimeCompiler: true, // See: https://vuejs.org/v2/guide/installation.html#Runtime-Compiler-vs-Runtime-only
  devServer: {
      writeToDisk: true, // Write files to disk in dev mode, so Django can serve the assets
  },
}; **/