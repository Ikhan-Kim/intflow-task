<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="8">
        <Video :video="url"/>
      </v-col>
      <v-col cols="12" md="2">
        <v-container fill-height class="btn">
          <camera-btn @CamNum='ChangeCam'/>
        </v-container>
      </v-col>
      <v-col cols="12" md="2">
        <v-container fill-height class="btn">
          <object-btn :buttonnum="numObject" @ObjNum='fillData' />
        </v-container>
      </v-col>
    </v-row>
    <div class="chartarea">
      <object-chart :chart-data="datacollection" :styles="myStyles"/>
    </div>
  </v-container>
</template>

<script>
import axios from 'axios'
import Video from '../components/Video.vue'
import CameraBtn from '../components/CameraBtn.vue'
import ObjectBtn from '../components/ObjectBtn.vue'
import ObjectChart from '../components/ObjectChart.vue'

const URL = 'http://127.0.0.1:5000/'

export default {
  name: 'Project',

  components: {
    Video,
    CameraBtn,
    ObjectBtn,
    ObjectChart,
  },

  data() {
    return {
      myStyles: {
        height: '300px',
        width: '100%',
        position: 'relative',
      },
      url: '9bDiPewdGPc',
      numObject: 4,
      CameraId: 1,
      ObjectId: 1,
      datacollection: {
        labels: ['a', 'b'],
        datasets: [
          {
            label: 'Data One',
            data: [0, 1]
          }
        ]
      },
      axiosData: {
        data: {
          'times': 0,
          'activity': 0,
          'feed': 0,
          'drinking': 0,
        }
      },
    }
  },
  mounted () {
      this.fillData(1)
  },
  methods: {
    ChangeCam(CameraId) {
      this.CameraId = CameraId
      if (CameraId === 1 ) {
        this.url = '9bDiPewdGPc'
      }
      else if (CameraId === 2) {
        this.url = 'rskJq-sfxyE'
      }
      else if (CameraId === 3) {
        this.url = 'MIB5PKnXUsw'
      }
      axios.get(URL + CameraId)
        .then((res) => {
          this.numObject = res.data[CameraId]
        })
    },

    fillData(ObjId) {
      axios.get(URL + this.CameraId + '/' + ObjId)
          .then((res) => {
            this.axiosData = res
          })
      this.datacollection = {
        labels: this.axiosData.data.times,
        datasets: [
          {
            label: 'activity',
            data: this.axiosData.data.activity,
            borderColor: 'red',
            pointBorderColor: 'red',
            pointBackgroundColor: 'red',
            fill:false
          },
          {
            label: 'feed',
            data: this.axiosData.data.feed,
            borderColor: 'yellow',
            pointBorderColor: 'yellow',
            pointBackgroundColor: 'yellow',
            fill:false
          },
          {
            label: 'drinking',
            data: this.axiosData.data.drinking,
            borderColor: 'blue',
            pointBorderColor: 'blue',
            pointBackgroundColor: 'blue',
            fill:false
          },
        ]
      }
    },
  }
}
</script>

<style>
  .btn {
    /* outline: 1px solid gray; */
    border: 1px solid gray;
    border-radius: 10px;
  }
</style>