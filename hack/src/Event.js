import React, { Component } from 'react';
import "./EvCard.css";

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
      return (
      <div>
      <p>test</p>
    </div>
      );
    }
  }

export default EvCard;