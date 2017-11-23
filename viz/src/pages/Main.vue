<template>
  <div class="main">
    <div class="background">
    </div>
    <div class="side-panel" id="side-panel">
      <img
        v-for="mitama in mitamas"
        class="side-logo"
        :class="{ 'side-logo-active': selected === mitama }"
        :src="require(`../assets/img/${mitama}.png`)"
        @click="mitamaSelect(mitama, $event)"
      >
    </div>
    <div class="stats-panel" :style="panelStyle">
      <div class="stats-left">
        <star-distribution :counts="starCounts">
        </star-distribution>
      </div>
      <div class="stats-right">
        <position-distribution :counts="positionCounts">
        </position-distribution>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import Vibrant from 'node-vibrant';
import StarDistribution from '@/components/StarDistribution';
import PositionDistribution from '@/components/PositionDistribution';

const metadata = require('@/assets/data.json');

export default {
  name: 'main',
  components: {
    'star-distribution': StarDistribution,
    'position-distribution': PositionDistribution,
  },
  data() {
    return {
      mitamas: ['三味', '火灵', '钟灵', '伤魂鸟', '狰', '铃女', '反枕', '珍珠', '镇墓兽', '地藏像', '破势', '镜姬', '天邪', '网切', '阴魔罗', '小袖之手', '薙魂', '雪幽魂', '心眼', '蚌精', '青鹭火', '招财猫', '蝠翼', '骰子鬼', '日女巳时', '被服', '魅妖', '木魅', '轮入道', '魍魉之匣', '树妖', '返魂香', '鸣屋', '涅槃之火', '针女'],
      selected: false,
      deferredSelected: false,
      styleFactors: {
        rotateDeg: 135,
        dark: [0, 0, 0],
        light: [50, 50, 50],
      },
    };
  },
  computed: {
    wrap() {
      if (this.selected) {
        return metadata[this.selected];
      }
      return metadata;
    },
    starCounts() {
      if (!this.wrap) {
        return [0, 0];
      }
      return [this.wrap['五星'], this.wrap['六星']];
    },
    positionCounts() {
      if (!this.wrap) {
        return [0, 0, 0, 0, 0, 0];
      }
      return [this.wrap['一号位'], this.wrap['二号位'], this.wrap['三号位'], this.wrap['四号位'], this.wrap['五号位'], this.wrap['六号位']];
    },
    panelStyle() {
      const factors = this.styleFactors;
      const dark = factors.dark;
      const light = factors.light;
      return `background-image: linear-gradient(${factors.rotateDeg}deg, rgba(${dark[0]}, ${dark[1]}, ${dark[2]}, 0.55), rgba(${light[0]}, ${light[1]}, ${light[2]}, 0.55));`;
    },
  },
  methods: {
    mitamaSelect(name, $event) {
      const vibrant = new Vibrant($event.target);
      vibrant.getPalette().then((palette) => {
        const { DarkVibrant, LightVibrant } = palette;
        const dark = DarkVibrant.getRgb();
        const light = LightVibrant.getRgb();
        this.styleFactors.dark = dark;
        this.styleFactors.light = light;
      });
      this.selected = this.selected !== name && name;
      Vue.nextTick(() => {
        setTimeout(() => {
          this.deferredSelected = this.selected;
        }, 200);
      });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import '../styles/constants.scss';

.background {
  background: rgb(53, 73, 94);
  width: 100vw;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  z-index: -1;
}

.main {
  .side-panel {
    position: fixed;
    height: 100vh;
    width: $side-panel-width;
    top: 0px;
    left: 0px;
    overflow: scroll;
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;

    .side-logo {
      transition: all 0.4s ease-in-out;
      width: 100px;
      cursor: pointer;
      filter: grayscale(100%);

      &:hover {
        filter: grayscale(60%);
      }

      &.side-logo-active {
        filter: none;
      }
    }
  }

  .stats-panel {
    margin: $stats-panel-margin;
    margin-left: $side-panel-width;
    padding: $stats-panel-margin;
    position: relative;
    display: flex;
    border-radius: 40px;
    height: calc(100vh - 4 * #{$stats-panel-margin});
    transition: background ease 1s;
  }

  .stats-right {
    display: flex;
    justify-content: center;
    align-items: center;
    height: inherit;
    width: calc(100vw - #{$side-panel-width} - 200px);
  }
}
</style>
