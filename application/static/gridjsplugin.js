import {BaseComponent, PluginPosition, h} from "https://unpkg.com/gridjs?module";


export class AddButtonPlugin extends BaseComponent {
    clickEvent = () => {
        this.config.eventEmitter.emit('plus-item', true)
    }

    render() {
        return h(
            'div',
            {class: 'd-flex justify-content-end align-items-center col'},
            [
                h('button', {class: 'btn text-secondary fs-2', onClick: this.clickEvent}, [
                    h('i', {class: 'bi bi-plus-square-fill'})
                ])
            ]
        );

    }
}

