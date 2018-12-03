<template>
  <div class="Q1Page">
    <h3>問題1</h3>
    <p>
      ユーザー名: {{ $route.params.username }}
    </p>
    aaa<el-slider v-model="value1"></el-slider>
    bbb<el-slider v-model="value2"></el-slider>
    ccc<el-slider v-model="value3"></el-slider>
    <button v-on:click="check">問題2に進む</button>
  </div>
</template>

<script>
import router from '../router'

export default {
  name: 'Q1Page',
  data () {
    return {
      value1: 0,
      value2: 0,
      value3: 0
    }
  },
  methods: {
    check: function (event) {
      var res = confirm(
        'aaa' + this.value1 + ' ポイント\n' +
        'bbb' + this.value2 + ' ポイント\n' +
        'ccc' + this.value3 + ' ポイント\n' +
        'よいですか？'
      )
      if (res === true) {
        router.push({name: 'Q2Page', params: {username: this.$route.params.username}})
      }
    }
  }
}
</script>

<style>
</style>
