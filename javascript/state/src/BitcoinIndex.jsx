import React, { useState, useEffect } from "react"


const BitcoinIndex = ({ currency="AUD" }) => {
  let [price, setPrice] = useState()

  // Only triggers on mount
  useEffect(() => {
    fetch(`http://api.coindesk.com/v1/bpi/currentprice/${currency}.json`)
      .then((res) => res.json())
      .then((data) => setPrice(data.bpi[currency].rate))

    // called on unmount
    // return () => {
    //   // cleanup code
    // }
  }, [currency])

  useEffect(() => console.log("effect triggered on mount or any change"))

  useEffect(() => console.log("effect triggered on mount or price change"), [price])

  return (
    <>
      <h1>Bitcoin Index</h1>
      {price ? <p>Current Price ({currency}): {price}</p> : <p>Loading ...</p>}
    </>
  )
}

export default BitcoinIndex