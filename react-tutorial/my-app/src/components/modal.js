function Modal(props) {

    function canclHander() {}

    function confirmHandler()


    return (
    <div className="modal">
        <p>Are you sure?</p>
        <button className="btn btn-alt" onClick={candelHander}>Cancel</button>
        <button className="btn">Confirm</button>
    </div>
    );
}

export default Modal;