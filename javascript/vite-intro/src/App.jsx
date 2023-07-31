import React from 'react'
import Comment from './Comment'
import Card from './Card'

const App = () => {
  return (
    <section>
        <Comment 
        avatar = "https://i.pravatar.cc/60?1"
        name="Mary Smith" 
        date="11/10/22" 
        comment="This is a comment" 
        >
            <h3>Hello</h3>
            <p>A better comment</p>
        </Comment>
        <Card>
            <Comment 
            avatar = "https://i.pravatar.cc/60?4"
            name="Joe Bloggs" 
            date="1/6/22" 
            comment="React is awesome!" 
            />
        </Card>
        <Comment 
        avatar = "https://i.pravatar.cc/60/?90"
        name="Jane Doe" 
        date="22/10/22" 
        comment="Couldn't agree more!" 
        />
    </section>
  )
}

export default App
