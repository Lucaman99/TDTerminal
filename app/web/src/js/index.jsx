import React from "react";
import ReactDOM from "react-dom";

import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import CircularProgress from 'material-ui/CircularProgress';

const $ = require("jquery");
import Bootstrap from 'bootstrap/dist/css/bootstrap.css';
import "../css/index.css"

import OutputPage from "./OutputPage.jsx";

class App extends React.Component {
	constructor(props){
		super(props);

		this.state = {
			name: "",
			results: false,
			data: [],
			content: null
		}

		this.changeContent = this.changeContent.bind(this);
		this.recordName = this.recordName.bind(this);
		this.submit = this.submit.bind(this);
	}

	recordName(event) {
		this.setState({name: event.target.value});
	}
	
	changeContent(content) {
		this.setState({
			content: content
		});
	}

	submit(event) {
		this.setState({
			content: (
				<div>
					<div style={{textAlign: "center"}}>
						<h3 style={{margin:5}}>Filter By...</h3>
						<button type="button" className="btn btn-primary" onClick={()=>this.submit("age")} style={{margin:5}}>Age</button>
						<button type="button" className="btn btn-primary" onClick={()=>this.submit("salary")} style={{margin:5}}>Salary</button>
					</div>
					<div className="mid">
						<table className="table">
							<thead>
								<tr>
									<th scope="col">Rank</th>
									<th scope="col">Age</th>
									<th scope="col">Customers</th>
									<th scope="col">Revenue Generated</th>
								</tr>
							</thead>
							<tbody>
								<td></td>
								<td></td>
								<td></td>
								<td></td>
							</tbody>
						</table>
						<div style={{left:"50%", display:"inline", position:"relative", marginLeft:-20}}>
							<CircularProgress size={60} thickness={5}/>
						</div>
					</div>
				</div>)
		})
		event.preventDefault();
		$.getJSON("/getMarkets?var=age&company=" + this.state.name, data => {
			this.setState({
				content: <OutputPage data={data} results={true} name={this.state.name}/>
			});
		}).fail(error =>{
			this.setState({
				content: <div style={{textAlign:"center", marginTop:20}}><h1>Company not found!</h1></div>
			})
		})
	}
	
	render() {
		return (
			<MuiThemeProvider>
				<nav className="navbar navbar-expand-lg navbar-dark bg-dark">
				  <a className="navbar-brand" href="#">TDTerminal</a>
				  <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
				    <span className="navbar-toggler-icon"></span>
				  </button>

				  <div className="collapse navbar-collapse" id="navbarSupportedContent">
				    <ul className="navbar-nav mr-auto">
				      <li className="nav-item dropdown">
				        <div className="dropdown-menu" aria-labelledby="navbarDropdown">
				          <a className="dropdown-item" href="#">Action</a>
				          <a className="dropdown-item" href="#">Another action</a>
				          <div className="dropdown-divider"></div>
				          <a className="dropdown-item" href="#">Something else here</a>
				        </div>
				      </li>
				    </ul>
				    <form className="form-inline my-2 my-lg-0" onSubmit={this.submit}>
						<input type="text"
							className="form-control mr-sm-2"
							placeholder="Company Name"
							aria-label="Company Name"
							aria-describedby="basic-addon1"
							onChange={this.recordName}
							value={this.state.name} />
				      <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
				    </form>
				  </div>
				</nav>
				{this.state.content}
			</MuiThemeProvider>
		);
	}
}

$(document).ready(()=>{
  const app = $("#app")[0];
  ReactDOM.render(<App clubName="mathletes"/>, app);
})