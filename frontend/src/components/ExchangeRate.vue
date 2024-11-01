<template>
  <div>
    <h2>현재 환율 정보</h2>
    <button @click="fetchExchangeRate">환율 가져오기</button>
    <div v-if="exchangeRate">
      <p>USD 기준 환율: {{ exchangeRate }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      exchangeRate: null,
    };
  },
  methods: {
    async fetchExchangeRate() {
      try {
        const response = await fetch("http://127.0.0.1:8000/accounts/get_exchange_rate/");
        const data = await response.json();
        // 예: USD에서 KRW 환율만 추출
        this.exchangeRate = data.rates.KRW;
      } catch (error) {
        console.error("환율 데이터를 가져오는 중 오류가 발생했습니다.", error);
      }
    },
  },
};
</script>
