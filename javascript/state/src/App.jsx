import React, { useState } from 'react'
import BitcointIndex from './BitcoinIndex.jsx'
import CurrencySelector from './CurrencySelector.jsx'

const App = () => {
  const [currency, setCurrency] = useState("AUD")

  return <>
    <BitcointIndex currency={currency} />
    <CurrencySelector currency={currency} setCurrency={setCurrency} />
  </>
}

export default App