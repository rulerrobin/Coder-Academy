import Greeting from "./Greeting"
import "./App.css"

const age = 10 * 5 

function App() {
  return (
    <>
      <h1>Hello</h1>
      <Greeting foo ="bar" name="Matt" age={age}/>
      <Greeting />
      <p>Lorem ipsum dolor</p>
      <Greeting />
    </>
    )
  }

export default App
