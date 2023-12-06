class hero {
  constructor(nome, idade, tipo) {
    this.nome = nome;
    this.idade = idade;
    this.tipo = tipo;
  }

  atacar() {
    switch (this.tipo) {
        case "mago":
            this.ataque = "magia";
            break;
        case "guerreiro":
            this.ataque = "espada"
            break;
        case "monge":
            this.ataque = "artes marciais"
            break;
        case "ninja":
            this.ataque = "shuriken"
            break;
        default:
            console.log("Escolha entre mago, guerreiro, monge ou ninja");
    }
    
    console.log(`O ${this.tipo} atacou usando ${this.ataque}`);
  }
}

let mago = new hero("Leandro", "27", "mago")
let guerreiro = new hero("Leandro", "27", "guerreiro")
let monge = new hero("Leandro", "27", "monge")
let ninja = new hero("Leandro", "27", "ninja")

mago.atacar()
guerreiro.atacar()
monge.atacar()
ninja.atacar()