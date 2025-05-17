// Hello 関数はパラメータの名前にあいさつを付けて返します
export function hello(name: string = 'world'): string {
  return `Hello, ${name}!`;
}

// デフォルトの挨拶を表示
console.log(hello());
