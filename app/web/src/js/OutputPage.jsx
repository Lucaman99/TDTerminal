import React from "react";
import ReactDOM from "react-dom";

const $ = require("jquery");
import Bootstrap from 'bootstrap/dist/css/bootstrap.css';
import "../css/index.css"

import CircularProgress from 'material-ui/CircularProgress';

export default class Result extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			value: "Age",
			data: this.props.data,
			loading: false
		}

		this.submit = this.submit.bind(this)
	}

	submit(val) {
		this.setState({
			loading: true,
			data: []
		})
		$.getJSON("/getMarkets?var=" + val.toLowerCase() + "&company=" + this.props.name, data => {
			this.setState({
				value: val[0].toUpperCase() + val.substring(1, val.length),
				data: data,
				loading: false
			});
		});
	}
	
	render() {
		return (
			<div>
				<div style={{textAlign: "center"}}>
					<h3 style={{margin:5}}>Filter By...</h3>
					<button type="button" className="btn btn-primary" onClick={()=>this.submit("age")} style={{margin:5}}>Age</button>
					<button type="button" className="btn btn-primary" onClick={()=>this.submit("salary")} style={{margin:5}}>Salary</button>
					<button type="button" className="btn btn-primary" onClick={()=>this.submit("occupation")} style={{margin:5}}>Occupation</button>
				</div>
				<div className="mid" style={{display: this.props.results ? "block" : "none"}}>
					<table className="table">
						<thead>
							<tr>
								<th scope="col">Rank</th>
								<th scope="col">{this.state.value}</th>
								<th scope="col">Customers</th>
								<th scope="col">Revenue Generated</th>
							</tr>
						</thead>
						<tbody>
						{
						this.state.data.map(({rank, value, quantity, revenue}) => {
							return (
								<tr>
									<th scope="row">{rank}</th>
									<td>{value}</td>
									<td>{quantity}</td>
									<td>${revenue}</td>
								</tr>
							)
						})
						}
						</tbody>
					</table>
					<div style={{display: this.state.loading ? "block" : "none"}}>
						<div style={{left:"50%", display:"inline", position:"relative", marginLeft:-20}}>
							<CircularProgress size={60} thickness={5}/>
						</div>
					</div>
				</div>
			</div>
		);
	}
}