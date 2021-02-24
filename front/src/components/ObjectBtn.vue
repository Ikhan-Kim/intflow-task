<template>
  <v-btn-toggle
    class="btn_layout"
    v-model="toggle_exclusive"
    mandatory
  >
    <v-row>
      <v-col cols="2" md="12" v-for="index in buttonnum" :key="index">
        <v-btn @click="ChangeObject(index)" block>
          {{ index }} 번
        </v-btn>
      </v-col>
    </v-row>
  </v-btn-toggle>
</template>

<script>
export default {
  name: 'ObjectBtn',

  props: {
    buttonnum: {
      type: Number,
    }
  },

  data () {
    return {
      toggle_exclusive: undefined,
    }
  },
  
  methods: {
    ChangeObject(num){
      this.$emit('ObjNum', num)
    }
  }
}
</script>

<style>
  .btn_layout {
    width: 100%;
  }
</style>