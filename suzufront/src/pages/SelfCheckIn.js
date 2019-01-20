
import React, { Component } from 'react';
import TodayEventWidget from "../widgets/TodayEventWidget";

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHome, faCheck, faMapMarkerAlt, faUserAlt } from '@fortawesome/free-solid-svg-icons'

class SelfCheckIn extends Component {

    constructor(props){
        super(props)
        this.state = {
            placeholderNome: "Digite seu nome aqui",
            nameNotFoundMsg: "Não encontrou seu nome? Aperte Enter para cadastrar.",
            nameNotFound: false,
            suggestions: [
                {name: 'Emil Yoshigae Nakao'},
                {name: 'Lia Yoshigae Nakao'},
            ]
        }
    }

    render(){
        return (
            <div role="main" class="container-fluid w-100 h-100 bg-dark">
                <div className="row h-100">
                    <div className="col-3 mr-n2">
                        <TodayEventWidget/>
                    </div>
                    <div className="col h-100">
                        <div className="card mt-2 mb-0 ml-n2 h-100">
                            <h5 className="card-header"><FontAwesomeIcon icon={faCheck}/> Marcar Presenças </h5>
                            <div className="card-body">
                                <input type="text" className="form-control form-control-lg mb-2" placeholder={this.state.placeholderNome}/>

                                {/* Caso nenhuma sugestão tenha sido encontrada, mostra msg */}
                                {this.state.nameNotFound &&
                                    <div className="text-center v-100"><i>{this.state.nameNotFoundMsg}</i></div>
                                }

                                {/* Lista de opções de nomes */}
                                {this.state.suggestions.map(function(suggestion, index){
                                    return <div className={"suzu-checkin-row highlight rounded"} >
                                        <h4>{suggestion.name}</h4>
                                        <button class="btn btn-outline-secondary btn-sm" ng-click="editYokoshi(yokoshi)"><span class="fa fa-pencil text-warning"></span> Corrigir Cadastro</button>
                                        <button class="btn btn-outline-secondary btn-sm" ng-click="cancelPresence(yokoshi)" ng-disabled="!isYokoshiPresent(yokoshi)"><span class="fa fa-minus-square text-danger"></span> Cancelar Presença</button>
                                        <button class="suzu-checkin-row-presencebtn btn btn-success float-right my-auto" ng-disabled="isYokoshiPresent(yokoshi)" ng-click="togglePresence(yokoshi)"><span class="fa fa-check"></span> Marcar Presença</button>

                                    </div>;
                                })}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default SelfCheckIn