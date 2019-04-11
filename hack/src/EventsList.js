import React, { Component } from 'react';
import logo from './logo.svg';
//import './App.css';
import EvCard from './EvCard';


class EventsList extends Component {

    constructor(props){
        super(props);
        this.state = {
            
        };
       
    }


  render() {
    var eventsArray = [{
        "name":"running",
        "description":"long run",
        "evPic":"null",
        "howFar":"5",
        "attending":"6",
        "required":"3"
    },{
        "name":"humusing",
        "description":"eating humus",
        "evPic":"null",
        "howFar":"12",
        "attending":"3",
        "required":"3"
        },{
            "name":"humusing",
            "description":"eating humus",
            "evPic":"null",
            "howFar":"12",
            "attending":"3",
            "required":"3"
            },{
                "name":"humusing",
                "description":"eating humus",
                "evPic":"null",
                "howFar":"12",
                "attending":"3",
                "required":"3"
                },{
                    "name":"humusing",
                    "description":"eating humus",
                    "evPic":"null",
                    "howFar":"12",
                    "attending":"3",
                    "required":"3"
                    },{
                        "name":"humusing",
                        "description":"eating humus",
                        "evPic":"null",
                        "howFar":"12",
                        "attending":"3",
                        "required":"3"
                        },{
                            "name":"humusing",
                            "description":"eating humus",
                            "evPic":"null",
                            "howFar":"12",
                            "attending":"3",
                            "required":"3"
                            },{
                                "name":"humusing",
                                "description":"eating humus",
                                "evPic":"null",
                                "howFar":"12",
                                "attending":"3",
                                "required":"3"
                                },{
                                    "name":"humusing",
                                    "description":"eating humus",
                                    "evPic":"null",
                                    "howFar":"12",
                                    "attending":"3",
                                    "required":"3"
                                    }];
       
      // var obj=JSON.parse(eventsArray);
        const s=[];
        var i;
      

        var arraylength = eventsArray.length;
      
for(let i=0;i<arraylength;i++){
    if(i%3===0){
        s.push(<tr></tr>);
    }
s.push(<th><EvCard name={eventsArray[i].name} description={eventsArray[i].description} howFar={eventsArray[i].howFar}  attending={eventsArray[i].attending}/></th>);

}
       //var rendering = <EvCard name={eventsArray[0].name} description={eventsArray[0].description} howFar={eventsArray[0].howFar}  attending={eventsArray[0].attending}/>
    return (
        <div>
        <table>
            <tbody>
        {s}
        </tbody>
      </table>
      </div>
    );
  }
}

export default EventsList;
