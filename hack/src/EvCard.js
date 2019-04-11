import React, { Component } from 'react';
import "./EvCard.css";
//import { Card, CardTitle, CardContent, CardAction, CardButton, CardImage } from 'react-native-material-cards'

class EvCard extends Component {

    constructor(props){
        super(props);
        this.state = {
            name : props.name,
            description : props.description,
            evPic : props.evPic,
            howFar : props.howFar, 
            attending : props.attending,
            required :  props.required
            
        };
    }

    
    render() {
      var snippet = [].slice.call(document.querySelectorAll('.hover'));
      if (snippet.length) {
        snippet.forEach(function (snippet) {
          snippet.addEventListener('mouseout', function (event) {
            if (event.target.parentNode.tagName === 'figure') {
              event.target.parentNode.classList.remove('hover')
            } else {
              event.target.parentNode.classList.remove('hover')
            }
          });
        });
      }

      return (
      <div>
      <figure class="snip1580"><img src="http://www.jbryant.eu/recipes/Humous.jpg" href="walla.co.il" alt="profile-sample2"/>
        <figcaption>
          <h3>{this.props.name}</h3>
          <h5>{this.props.description}</h5>
          <h6>{this.props.howFar} KM from your location</h6>
          <h5>{this.props.attending}/{this.props.required}</h5>
        </figcaption><a href="#"></a>
      </figure>
    </div>
      );
    }
  }

export default EvCard;