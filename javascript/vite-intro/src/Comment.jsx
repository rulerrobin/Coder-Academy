import React from 'react'

const Comment = ({ name, date, comment, avatar, children }) => {
  return (
    <article>
        <header>
            <img src={avatar} alt="" />
            <p>{name}</p>
            <time>{date}</time>
        </header>
        {children}
        <p>{comment}</p>
        <hr />
    </article>
  )
}

export default Comment