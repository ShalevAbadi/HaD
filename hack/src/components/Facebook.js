import React, { Component } from 'react'
import FacebookLogin from 'react-facebook-login'
import './Facebook.css';
export default class Facebook extends Component {
    state = {
        isLoggedIn: false,
        userID: '',
        name: '',
        email: '',
        picture: ''
    };

    responseFacebook = response => {
        //console.log(response);

        this.setState({
            isLoggedIn: true,
            userID: response.userID,
            name: response.name,
            email: response.email,
            picture: response.picture.data.url
        });
    };

    componentClicked = () => console.log("Clicked");


    render() {
        let fbContent;

        if (this.state.isLoggedIn) {
            fbContent = (
                <div style={{
                    width: '400px',
                    margin: 'auto',
                    background: '#f4f4f4',
                    padding: '20px',
                }}>

                    <img id='avatar' src={this.state.picture} alt={this.state.name}/>
                    <h2>Welcome {this.state.name}</h2>
                    Email: {this.state.email}
                </div>
            );
        } else {
            fbContent = (<FacebookLogin
                appId="1341031156021973"
                autoLoad={true}
                fields="name,email,picture"
                onClick={this.componentClicked}
                callback={this.responseFacebook} />);
        }


        return (
            <div>
                {fbContent}
             </div>
            
            )
    }
}