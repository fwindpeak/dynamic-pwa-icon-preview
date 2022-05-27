<script setup lang="ts">
const pwaFilePath = '/pwa-512x512.png'
</script>

<template>
  <div>
    <div text-4xl>
      动态PWA图标测试
    </div>

    <div flex justify="center">
      <img :src="pwaFilePath" w-256px h-256px>
    </div>

    <div flex justify-center>
      <form action="/upload" method="post" enctype="multipart/form-data">
        选择文件 : <input type="file" name="file">
        <input type="submit" value="点击上传" btn block my-4>
      </form>
    </div>

    <div py-4 opacity-75>
      上传后点一下刷新，Safari->添加到主屏幕
    </div>
  </div>
</template>

<route lang="yaml">
meta:
  layout: home
</route>
