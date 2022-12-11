import React from 'react'
import axios from 'axios'
import loading from '../load.gif'
import Button from "components/CustomButtons/Button.js";
import Card from "components/Card/Card.js";
import CardHeader from "components/Card/CardHeader.js";
import CardBody from "components/Card/CardBody.js";
import { toast } from 'react-toastify'
import "react-toastify/dist/ReactToastify.css"
toast.configure();


export default class UserProfile extends React.Component {

  state = {
    amount: '',
    strategyOne: '',
    strategyTwo: '',
    strategies: ['Ethical Investing', 'Growth Investing', 'Index Investing', 'Quality Investing', 'Value Investing'],
    availableSecondStrategies: [],
    result: [],
    loading: false
  }

  componentDidMount = () => {
    localStorage.clear()
  }

  onAmountChange = (e) => {
    e.preventDefault()
    e.persist()
    this.setState(() => ({ amount: e.target.value }))
  }

  onStrategyOneChange = (e) => {
    e.preventDefault()
    e.persist()

    const availableSecondStrategies = this.state.strategies.filter((strategy) => strategy !== e.target.value)
    this.setState(() => ({ strategyOne: e.target.value, availableSecondStrategies, strategyTwo: 'DEFAULT' }))
  }

  onStrategyTwoChange = (e) => {
    e.preventDefault()
    e.persist()
    this.setState(() => ({ strategyTwo: e.target.value }))
  }

  handleOnSubmit = async (e) => {
    e.preventDefault()
    if (this.state.amount === '') return toast('Enter Amount', { type: 'warning' })
    if (!this.state.strategyOne) return toast('Atleast 1 strategy required', { type: 'warning' })
    localStorage.clear()
    //Need to get the axios call here
    this.setState(() => ({ loading: true }))

    const result = (await axios.post('http://localhost:5000/stocksuggestion', { amount: this.state.amount, strategies: this.state.strategyOne + (this.state.strategyTwo !== 'DEFAULT' ? ',' + this.state.strategyTwo : '') })).data.result
    this.setState(() => ({ result, loading: false }))
    localStorage.setItem('result', JSON.stringify(result))
    this.props.history.push({
      pathname: '/admin/dashboard',
      state: 'test'
    })
  }
  render() {
    return (
      <div>

        <Card>
          <CardHeader color="danger">
            <h4 className="cardTitleWhite">Enter Your Preference</h4>
          </CardHeader>
          <CardBody>
            <form onSubmit={this.handleOnSubmit}>
              <div className="form-group">
                <label htmlFor="exampleInputEmail1">Investment Amount</label>
                <input
                  type="number"
                  className="form-control"
                  id="exampleInputEmail1"
                  aria-describedby="emailHelp"
                  placeholder="Amount in USD"
                  min={5000}
                  value={this.state.amount}
                  onChange={this.onAmountChange}
                />
              </div>
              <div className="form-group">
                <label htmlFor="exampleFormControlSelect1">Investment Strategy 1</label>
                <select className="form-control" id="exampleFormControlSelect1" onChange={this.onStrategyOneChange} defaultValue={'DEFAULT'}>
                  <option value="DEFAULT" disabled>Select Your Preferred Investment Strategy</option>
                  {
                    this.state.strategies.map((strategy) => <option key={strategy} value={strategy}>{strategy}</option>)
                  }
                </select>
              </div>

              {<div className="form-group">
                <label htmlFor="exampleFormControlSelect1">Investment Strategy 2</label>
                <select className="form-control" id="exampleFormControlSelect1" onChange={this.onStrategyTwoChange} defaultValue={"DEFAULT"}>
                  <option value="DEFAULT" disabled>Select Your Preferred Investment Strategy</option>
                  {
                    this.state.availableSecondStrategies.map((availableStrategy) => <option key={availableStrategy} value={availableStrategy}>{availableStrategy}</option>)
                  }
                </select>
              </div>}

              <Button type="submit" color="info" >Show Strategy</Button>
            </form>
          </CardBody>
        </Card>
        <div className="loading" style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
        }}>{this.state.loading && <img src={loading} alt="alt"></img>}</div>
      </div>
    )
  }
}