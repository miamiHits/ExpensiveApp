import React, { Component } from 'react';

class Card extends Component{
    render(){
        return (
       <React.Fragment>
        <section className="card-continer">
        <header>
            <span initials="RonP_YardenC"></span>
            <h2>Expenses App</h2>
        </header>
        <main>
            <ul>
                <li><span>Will document all your expenses</span></li>
                
            </ul>
        </main>
        </section>
       </React.Fragment> 
        )
    }
}

export default Card;