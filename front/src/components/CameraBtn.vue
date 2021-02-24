<template>
  <v-btn-toggle
    class="btn_layout"
    v-model="toggle_exclusive"
    mandatory
  >
    <v-row>
      <v-col cols="2" md="12">
        <v-btn @click="ChangeCam(1)" block>
          1번 CAM
        </v-btn>
      </v-col>
      <v-col cols="2" md="12">
        <v-btn @click="ChangeCam(2)" block>
          2번 CAM
        </v-btn>
      </v-col>
      <v-col cols="2" md="12">
        <v-btn @click="ChangeCam(3)" block>
          3번 CAM
        </v-btn>
      </v-col>
    </v-row>
  </v-btn-toggle>
</template>

<script>
export default {
name: 'CameraBtn',

  data () {
    return {
      toggle_exclusive: undefined,
    }
  },

  methods: {
    ChangeCam(num) {
      this.$emit('CamNum', num)
      // console.log(num)
    }
  }
}
</script>

<style>
  .btn_layout {
    width: 100%;
  }
</style>