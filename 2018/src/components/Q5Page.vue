<template>
  <div class="QPage">
    <h3>問題5: せせらぎバトル(バランス)</h3>
    <p>
      ユーザー名: {{ $route.params.username }}
    </p>
    aaa<el-slider v-model="value1"></el-slider>
    bbb<el-slider v-model="value2"></el-slider>
    ccc<el-slider v-model="value3"></el-slider>
    ddd<el-slider v-model="value4"></el-slider>
    <button v-on:click="check">回答して次の問題に進む</button>
  </div>
</template>

<script>
import router from '../router'
import firebase from 'firebase'

export default {
  name: 'Q5Page',
  data () {
    return {
      value1: 0,
      value2: 0,
      value3: 0,
      value4: 0
    }
  },
  methods: {
    check: function (event) {
      var res = confirm(
        'aaa: ' + this.value1 + ' ポイント\n' +
        'bbb: ' + this.value2 + ' ポイント\n' +
        'ccc: ' + this.value3 + ' ポイント\n' +
        'ddd: ' + this.value4 + ' ポイント\n' +
        'よいですか？'
      )
      if (res === true) {
        this.database = firebase.database()
        this.bounenRef = this.database.ref('bounen/' + this.$route.params.username)
        this.bounenRef.update({
          Q5: {
            1: this.value1,
            2: this.value2,
            3: this.value3,
            4: this.value4
          }
        })
        router.push({name: 'Q6Page', params: {username: this.$route.params.username}})
      }
    }
  }
}
</script>

<style>
</style>
