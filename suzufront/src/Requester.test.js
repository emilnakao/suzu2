

it('forwards get calls completing the url', () => {
    const spy = jest.spyOn(axios, 'get').mockImplementation(() => Promise.resolve({ success: true }))


    expect(spy).toHaveBeenCalled()
    spy.mockRestore
});