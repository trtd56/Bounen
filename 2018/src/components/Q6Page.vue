<template>
  <div class="QPage">
    <p>ユーザー名: {{ $route.params.username }}</p>
    <h3>問題6: せせらぎバトル(スピード)</h3>
    <p>誰に賭ける？</p>
    <table align="center">
    <tr>
    <td width="50">aaaa</td>
    <td width="120"><el-slider v-model="value1"></el-slider></td>
    <td width="50">{{ value1 }}</td>
    </tr>
    <tr>
    <td width="50">bbbb</td>
    <td width="120"><el-slider v-model="value2"></el-slider></td>
    <td width="50">{{ value2 }}</td>
    </tr>
    <tr>
    <td width="50">cccc</td>
    <td width="120"><el-slider v-model="value3"></el-slider></td>
    <td width="50">{{ value3 }}</td>
    </tr>
    <tr>
    <td width="50">dddd</td>
    <td width="120"><el-slider v-model="value4"></el-slider></td>
    <td width="50">{{ value4 }}</td>
    </tr>
    </table>
    <button v-on:click="check">回答して終わる</button>
  </div>
</template>

<script>
import router from '../router'
import firebase from 'firebase'

export default {
  name: 'Q6Page',
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
          Q6: {
            1: this.value1,
            2: this.value2,
            3: this.value3,
            4: this.value4
          }
        })
        router.push({name: 'TopPage', params: {}})
      }
    }
  }
}
</script>

<style>
</style>
