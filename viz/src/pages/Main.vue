<template>
  <div class="main">
    <div class="background">
      <img
        id="mitama-background"
        :src="require(`../assets/img/${deferredSelected}.png`)"
      >
    </div>
    <div class="side-panel" id="side-panel">
      <img
        v-for="mitama in mitamas"
        class="side-logo"
        :class="{ 'side-logo-active': selected === mitama }"
        :src="require(`../assets/img/${mitama}.png`)"
        @click="mitamaSelect(mitama)"
      >
    </div>
    <div class="stats-panel">
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
  },
  methods: {
    mitamaSelect(name) {
      this.selected = this.selected !== name && name;
      Vue.nextTick(() => {
        const ele = document.getElementById('mitama-background');
        ele.classList.add('super-blur');
        setTimeout(() => {
          this.deferredSelected = this.selected;
          ele.classList.remove('super-blur');
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

  img {
    transform: translateZ(0);
    will-change: transform;
    width: 100vw;
    margin-top: calc((100vh - 100vw) / 2);
    transition: all ease-in-out .5s;
    filter: blur(80px);

    &.super-blur {
      filter: blur(200px);
    }
  }
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
    margin-left: $side-panel-width;
    display: flex;
  }

  .stats-right {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: calc(100vw - #{$side-panel-width} - 200px);
  }
}
</style>
