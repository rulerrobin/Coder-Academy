import React from 'react'

const styles = {
   border: '2px solid white',
   padding: '0.5rem',
   margin: '0.5rem',
   borderRadius: '0.5rem'
}

const Card = ({ children }) => {
  return (
    <div style={styles}>{children}</div>
  )
}

export default Card