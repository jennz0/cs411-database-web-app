$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    $('#task-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes

        const modal = $(this)
        if (taskID === 'New Model') {
            modal.find('.modal-title').text(taskID)
            $('#task-form-display').removeAttr('taskID')
        } else {
            modal.find('.modal-title').text('Edit Price Model ' + taskID)
            $('#task-form-display').attr('taskID', taskID)
        }

        if (content) {
            modal.find('.form-control').val(content);
        } else {
            modal.find('.form-control').val('');
        }
    })


    $('#submit-task').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        console.log($('#task-modal').find('.form-control').val())
        $.ajax({
            type: 'POST',
            url: tID ? '/edit/' + tID : '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#task-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });
    // search:
    $('#search-task').click(function () {
        console.log($('#search-modal').find('.form-control').val())
        $.ajax({
            type: 'POST',
            url: '/search',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#search-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });
    //end search
    // advance:
    $('#advance-task').click(function () {
        $.ajax({
            type: 'POST',
            url: '/advance',
            contentType: 'application/json;charset=UTF-8',
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });
    //end advance   

    // procedure:
    $('#procedurecpu-task').click(function () {
        $.ajax({
            type: 'POST',
            url: '/cpuprocedure',
            contentType: 'application/json;charset=UTF-8',
            success: function (res) {
                console.log(res.response) 
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });
    //end procedure  

    $('.remove').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#Office').click(function(){
        console.log(this.innerHTML)
        $.ajax({
            type: 'POST',
            url: '/purpose',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': 'office'
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    })

    $('#Gaming').click(function(){
        console.log(this.innerHTML)
        $.ajax({
            type: 'POST',
            url: '/purpose',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': 'game'
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    })

    $('#Server').click(function(){
        console.log(this.innerHTML)
        $.ajax({
            type: 'POST',
            url: '/purpose',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': 'server'
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();

            },
            error: function () {
                console.log('Error');
            }
        });
    })

    $('#All').click(function(){
        console.log(this.innerHTML)
        $.ajax({
            type: 'POST',
            url: '/purpose',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': 'all'
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();

            },
            error: function () {
                console.log('Error');
            }
        });
    })

    $('.select').click(function(){
        const select = $(this)
        console.log('print')
        console.log(select.data('source'))

        $.ajax({
            type: 'POST',
            url: '/select/' + select.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    })
    
});