<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
*, *::before, *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body {
  width: 100%;
  height: 100%;
}

#app {
  width: 100%;
  min-height: 100%;
  overflow: hidden;
  background-size: 20px 20px;
  background-image: linear-gradient(
    -45deg,
    white 0%, white 10%,
    mistyrose 10%, mistyrose 50%,
    white 50%, white 60%,
    mistyrose 60%, mistyrose 100%
  );
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  text-align: center;
}

#app > div {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 100%;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 4px 16px;
  background: darkorange;
  color: white;
}

.header h1 {
  font-size: 24px;
}

.contents {
  display: flex;
  flex-direction: column;
  align-content: center;
  flex-grow: 1;
  margin: 24px auto;
  padding: 8px 0 4px;
  width: 90%;
  background-color: rgba(255, 255, 255, 0.9);
}

.contents h2 {
  position: relative;
  height: 34px;
  line-height: 34px;
  font-size: 16px;
  border-bottom: darkorange solid 2px;
  margin: 0 16px 16px;
  padding: 0 8px;
}

.contents h2::before {
  display: block;
  position: absolute;
  left: -8px;
  width: 8px;
  height: 100%;
  background: linear-gradient(
    90deg,
    darkorange 0%, darkorange 40%,
    transparent 40%, transparent 60%,
    darkorange 60%, darkorange 100%);
  content: "";
}

button {
  display: block;
  width: auto;
  margin: 0 auto;
  padding: 4px 8px;
  cursor: pointer;
  outline: none;
  appearance: none;
  border: solid 2px lightgray;
  background-color: white;
}

.QPage > .contents button {
  margin-top: 4px;
}

table {
  border: 2px solid darkgray;
  border-radius: 3px;
  background-color: #fff;
  margin: 0 4px;
}

th {
  background-color: darkorange;
  color: rgba(255,255,255,0.66);
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  padding: 16px;
}

td {
  background-color: #f9f9f9;
  padding: 8px 16px;
}

td:nth-child(1) {
  width: 92px;
}

td:nth-child(3) {
  width: 64px;
}
</style>
